"""
Modulo de Servicios - Reportes
Define la logica de generacion de reportes y analisis
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
from ..models.producto import Producto
from ..repositories.inventario import Inventario


class GeneradorReportes:
    """
    Genera reportes del inventario.
    Responsable de analisis y estadisticas.
    """
    def __init__(self, inventario: Inventario):
        """Inicializa el generador de reportes."""
        self.inventario = inventario

    def valor_total_inventario(self) -> float:
        """Calcula el valor total del inventario."""
        productos = self.inventario.repositorio.obtener_todos()
        return sum(p.calcular_valor_total() for p in productos)

    def cantidad_total_productos(self) -> int:
        """Cuenta la cantidad total de productos."""
        return len(self.inventario.repositorio.obtener_todos())
