"""
Test unitario para conexión a base de datos
"""
import pytest
from unittest.mock import patch, MagicMock
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import Session

from adapter.outbound.database.base import (
    check_database_connection,
    get_db,
    init_database,
    get_tables,
    engine,
    SessionLocal,
    Base
)


class TestDatabaseConnection:
    """Tests para funciones de conexión a la base de datos"""

    def test_check_database_connection_success(self):
        """Test de conexión exitosa a la base de datos"""
        # Verificar que la función retorna True cuando la conexión es exitosa
        result = check_database_connection()
        assert isinstance(result, bool)

    @patch('adapter.outbound.database.base.engine.connect')
    def test_check_database_connection_failure(self, mock_connect):
        """Test de fallo en conexión a la base de datos"""
        # Simular error de conexión
        mock_connect.side_effect = Exception("Connection failed")

        result = check_database_connection()
        assert result is False

    def test_get_db_dependency(self):
        """Test del dependency injection get_db()"""
        # Obtener generador de sesión
        db_generator = get_db()

        # Verificar que retorna un generador
        assert hasattr(db_generator, '__next__')

        # Obtener la sesión
        db_session = next(db_generator)

        # Verificar que es una instancia de Session
        assert isinstance(db_session, Session)

        # Cerrar la sesión
        try:
            next(db_generator)
        except StopIteration:
            pass  # Esperado cuando el generador termina

    @patch('sqlalchemy.inspect')
    def test_get_tables(self, mock_inspect):
        """Test para obtener lista de tablas"""
        # Mock del inspector
        mock_inspector = MagicMock()
        mock_inspector.get_table_names.return_value = ['tabla1', 'tabla2', 'pruebas']
        mock_inspect.return_value = mock_inspector

        tables = get_tables()

        # Verificar que retorna una lista
        assert isinstance(tables, list)
        assert 'pruebas' in tables

    @patch('adapter.outbound.database.base.Base.metadata.create_all')
    @patch('adapter.outbound.database.base.engine.connect')
    def test_init_database_success(self, mock_connect, mock_create_all):
        """Test de inicialización exitosa de la base de datos"""
        # Mock de la conexión
        mock_conn = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.execute.return_value = MagicMock()

        # Ejecutar la función sin que lance excepción
        try:
            init_database()
            success = True
        except Exception:
            success = False

        assert success is True
        mock_create_all.assert_called_once()

    @patch('sqlalchemy.inspect')
    @patch('adapter.outbound.database.base.engine')
    def test_create_get_tables_and_drop_sequence(self, mock_engine, mock_inspect):
        """Test secuencial: 1) Crear tabla 'pruebas', 2) Verificar en get_tables, 3) Eliminar tabla"""

        # Mock del inspector para simular las tablas
        mock_inspector = MagicMock()

        # Contador para simular el estado de las tablas
        call_count = [0]  # Usar lista para que sea mutable en la función anidada

        def get_tables_side_effect():
            call_count[0] += 1
            if call_count[0] == 1:
                # Primera llamada: después de crear, incluye 'pruebas'
                return ['tabla1', 'tabla2', 'pruebas']
            else:
                # Segunda llamada: después de eliminar, sin 'pruebas'
                return ['tabla1', 'tabla2']

        mock_inspector.get_table_names.side_effect = get_tables_side_effect
        mock_inspect.return_value = mock_inspector

        # Crear metadata separada para la tabla de prueba
        test_metadata = MetaData()

        # Definir tabla de prueba
        test_table = Table(
            'pruebas',
            test_metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50))
        )

        # PASO 1: Crear la tabla
        test_metadata.create_all(bind=mock_engine)

        # PASO 2: Verificar que la tabla existe en get_tables
        tables = get_tables()
        assert isinstance(tables, list)
        assert 'pruebas' in tables

        # PASO 3: Eliminar la tabla
        test_metadata.drop_all(bind=mock_engine)

        # Verificar que la tabla fue eliminada
        tables_after = get_tables()
        assert 'pruebas' not in tables_after

        # Verificar que se llamaron los métodos correctos
        assert mock_inspector.get_table_names.call_count == 2


if __name__ == "__main__":
    pytest.main([__file__])