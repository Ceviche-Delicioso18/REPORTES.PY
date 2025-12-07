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
    
    def total_items_stock(self) -> int:
        """Calcula el total de items en stock."""
        productos = self.inventario.repositorio.obtener_todos()
        return sum(p.cantidad for p in productos)
    
    def producto_mas_caro(self) -> Optional[Producto]:
        """Obtiene el producto mas caro."""
        productos = self.inventario.repositorio.obtener_todos()
        return max(productos, key=lambda p: p.precio) if productos else None

    def producto_mas_barato(self) -> Optional[Producto]:
        """Obtiene el producto mas barato."""
        productos = self.inventario.repositorio.obtener_todos()
        return min(productos, key=lambda p: p.precio) if productos else None

