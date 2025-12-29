#!/usr/bin/env python3
"""
Pizza Value Calculator
Finds the best pizza-to-price ratio based on pizza area and cost.
"""

import math


class Pizza:
    """Represents a pizza with size and price information."""
    
    def __init__(self, name, size, price):
        """
        Initialize a pizza.
        
        Args:
            name (str): Name of the pizza
            size (str or float): Either diameter in cm (e.g., "26cm" or 26) 
                                or dimensions for rectangular pizza (e.g., "46x33cm")
            price (float): Price in euros
        """
        self.name = name
        self.price = price
        self.area = self._calculate_area(size)
        self.value_ratio = self.area / self.price if self.price > 0 else 0
    
    def _calculate_area(self, size):
        """
        Calculate pizza area based on size specification.
        
        Args:
            size (str or float): Size specification
            
        Returns:
            float: Area in square centimeters
        """
        if isinstance(size, (int, float)):
            # Assume it's a diameter for round pizza
            radius = size / 2
            return math.pi * radius ** 2
        
        size_str = str(size).lower().replace('cm', '').strip()
        
        if 'x' in size_str:
            # Rectangular pizza
            dimensions = size_str.split('x')
            width = float(dimensions[0].strip())
            height = float(dimensions[1].strip())
            return width * height
        else:
            # Round pizza (diameter)
            diameter = float(size_str)
            radius = diameter / 2
            return math.pi * radius ** 2
    
    def __str__(self):
        return (f"{self.name}: {self.area:.2f} cm² for €{self.price:.2f} "
                f"(€{self.price/self.area*100:.2f} per 100 cm²)")
    
    def __repr__(self):
        return f"Pizza('{self.name}', area={self.area:.2f}, price={self.price:.2f})"


def find_best_pizza(pizzas):
    """
    Find the pizza with the best value (highest area per euro).
    
    Args:
        pizzas (list): List of Pizza objects
        
    Returns:
        Pizza: The pizza with the best value ratio
    """
    return max(pizzas, key=lambda p: p.value_ratio)


def display_results(pizzas):
    """
    Display all pizzas ranked by value.
    
    Args:
        pizzas (list): List of Pizza objects
    """
    sorted_pizzas = sorted(pizzas, key=lambda p: p.value_ratio, reverse=True)
    
    print("=" * 70)
    print("PIZZA VALUE ANALYSIS")
    print("=" * 70)
    print()
    
    for i, pizza in enumerate(sorted_pizzas, 1):
        print(f"{i}. {pizza.name}")
        print(f"   Area: {pizza.area:.2f} cm²")
        print(f"   Price: €{pizza.price:.2f}")
        print(f"   Value: {pizza.value_ratio:.2f} cm² per €")
        print(f"   Cost: €{pizza.price/pizza.area*100:.2f} per 100 cm²")
        print()
    
    best = sorted_pizzas[0]
    print("=" * 70)
    print(f"🍕 BEST VALUE: {best.name}")
    print(f"   You get {best.value_ratio:.2f} cm² per euro!")
    print("=" * 70)


def main():
    """Main function to run the pizza value calculator."""
    
    # Define the pizzas based on the provided data
    pizzas = [
        Pizza("Small Pizza", "26cm", 4.80),
        Pizza("Large Pizza", "30cm", 5.50),
        Pizza("Party Pizza", "46x33cm", 13.00)
    ]
    
    # Display results
    display_results(pizzas)
    
    # Calculate budget recommendations
    print("\n" + "=" * 70)
    print("BUDGET RECOMMENDATIONS")
    print("=" * 70)
    
    best = find_best_pizza(pizzas)
    budget = 20.00  # Example budget
    
    print(f"\nWith a budget of €{budget:.2f}:")
    num_pizzas = int(budget / best.price)
    total_area = num_pizzas * best.area
    leftover = budget - (num_pizzas * best.price)
    
    print(f"  → Buy {num_pizzas}x {best.name}")
    print(f"  → Total pizza area: {total_area:.2f} cm²")
    print(f"  → Leftover: €{leftover:.2f}")


if __name__ == "__main__":
    main()