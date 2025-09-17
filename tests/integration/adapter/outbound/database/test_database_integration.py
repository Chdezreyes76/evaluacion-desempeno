"""
Test de integración para conexión REAL a base de datos
⚠️ Requiere que la base de datos esté corriendo y accesible
"""
import pytest
from sqlalchemy import MetaData, Table, Column, Integer, String, text
from sqlalchemy.orm import Session

from adapter.outbound.database.base import (
    check_database_connection,
    get_db,
    get_tables,
    engine,
    SessionLocal
)


class TestDatabaseIntegration:
    """Tests de integración con conexión real a la base de datos"""

    def test_real_database_connection(self):
        """Test 1: Verificar conexión real a la base de datos"""
        result = check_database_connection()

        # Si falla aquí, la BD no está disponible o las credenciales son incorrectas
        assert result is True, "No se pudo conectar a la base de datos real"

    def test_real_get_db_session(self):
        """Test 2: Verificar que get_db() retorna sesión real funcional"""
        # Obtener generador de sesión
        db_generator = get_db()

        # Obtener la sesión real
        db_session = next(db_generator)

        # Verificar que es una instancia de Session
        assert isinstance(db_session, Session)

        # Probar que la sesión funciona ejecutando una query simple
        try:
            result = db_session.execute(text("SELECT 1 as test"))
            row = result.fetchone()
            assert row[0] == 1, "La sesión de BD no ejecuta queries correctamente"
        finally:
            # Cerrar la sesión
            try:
                next(db_generator)
            except StopIteration:
                pass  # Esperado cuando el generador termina

    def test_real_get_tables(self):
        """Test 3: Verificar que get_tables() retorna lista real de tablas"""
        tables = get_tables()

        # Verificar que retorna una lista
        assert isinstance(tables, list), "get_tables() no retorna una lista"

        # En una BD nueva puede estar vacía, pero debe ser una lista válida
        print(f"📋 Tablas encontradas: {tables}")

    def test_real_create_verify_drop_table_sequence(self):
        """Test 4: SECUENCIA REAL - Crear tabla 'pruebas' → Verificar → Eliminar"""

        # Crear metadata separada para la tabla de prueba
        test_metadata = MetaData()

        # Definir tabla de prueba
        test_table = Table(
            'pruebas',
            test_metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50)),
            Column('descripcion', String(200))
        )

        try:
            # PASO 1: Crear la tabla REAL
            print("🔨 Creando tabla 'pruebas'...")
            test_metadata.create_all(bind=engine)

            # PASO 2: Verificar que la tabla existe REALMENTE
            print("🔍 Verificando que la tabla existe...")
            tables = get_tables()
            assert 'pruebas' in tables, f"La tabla 'pruebas' no fue creada. Tablas: {tables}"
            print(f"✅ Tabla 'pruebas' encontrada en: {tables}")

            # PASO 3: Probar que podemos usar la tabla (insertar/consultar)
            print("💾 Probando insertar datos en la tabla...")
            with SessionLocal() as db:
                # Insertar un registro de prueba
                db.execute(text("INSERT INTO pruebas (name, descripcion) VALUES ('test', 'prueba de integración')"))
                db.commit()

                # Consultar el registro
                result = db.execute(text("SELECT COUNT(*) FROM pruebas"))
                count = result.scalar()
                assert count >= 1, "No se pudo insertar datos en la tabla"
                print(f"✅ Datos insertados correctamente. Registros: {count}")

            # PASO 4: Eliminar la tabla REAL
            print("🗑️ Eliminando tabla 'pruebas'...")
            test_metadata.drop_all(bind=engine)

            # PASO 5: Verificar que la tabla fue eliminada REALMENTE
            print("🔍 Verificando que la tabla fue eliminada...")
            tables_after = get_tables()
            assert 'pruebas' not in tables_after, f"La tabla 'pruebas' no fue eliminada. Tablas: {tables_after}"
            print(f"✅ Tabla 'pruebas' eliminada correctamente. Tablas restantes: {tables_after}")

        except Exception as e:
            # LIMPIEZA: En caso de error, intentar eliminar la tabla
            print(f"❌ Error durante el test: {e}")
            try:
                print("🧹 Intentando limpiar tabla 'pruebas'...")
                test_metadata.drop_all(bind=engine)
                print("✅ Limpieza completada")
            except Exception as cleanup_error:
                print(f"⚠️ Error durante limpieza: {cleanup_error}")

            # Re-lanzar el error original
            raise e

    def test_real_session_transaction(self):
        """Test 5: Verificar que las transacciones funcionan correctamente"""
        db = SessionLocal()

        try:
            # Probar transacción simple
            result = db.execute(text("SELECT 1 as test"))
            row = result.fetchone()
            assert row[0] == 1

            # Probar commit
            db.commit()

        except Exception as e:
            # Probar rollback
            db.rollback()
            raise e
        finally:
            db.close()


if __name__ == "__main__":
    # Configurar pytest para mostrar más detalles
    pytest.main([__file__, "-v", "-s"])  # -s para ver los prints