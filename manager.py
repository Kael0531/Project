from models import ElectronicProduct, OutdoorProduct
from algorithms import SKUTrie, heap_sort_by_stock

class InventoryManager:
    def __init__(self):
        self.inventory = []
        self.sku_trie = SKUTrie()  # Initialize the Trie Data Structure
        self.action_logs = []      # New Feature: System logging
        self._load_initial_data()

    def _log_action(self, message: str):
        """Private method to record system events."""
        self.action_logs.append(message)

    def _load_initial_data(self):
        """Pre-load data and populate both List and Trie."""
        charger1 = ElectronicProduct("EL-001", "120W MSI Laptop Charger", 45.99, 150, "19.5V")
        charger2 = ElectronicProduct("EL-002", "180W Gaming Adapter", 65.50, 10, "19.5V") # Low stock test
        repeller = OutdoorProduct("OUT-001", "Solar Mosquito Repeller", 25.99, 300, "IP65")
        
        products = [charger1, charger2, repeller]
        self.inventory.extend(products)
        
        for p in products:
            self.sku_trie.insert(p) # Insert into Trie for fast searching
            
        self._log_action("System Initialized with 3 default products.")

    def show_all_products(self):
        print("\n--- Current Amazon/Taobao Inventory ---")
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for item in self.inventory:
                print(item.display_info())
        print("---------------------------------------\n")

    def update_stock(self, sku: str, new_stock: int):
        # We can optimize this by searching directly in Trie if we wanted exact match,
        # but iterating list works for simplicity here.
        for item in self.inventory:
            if item.get_sku() == sku:
                try:
                    item.set_stock(new_stock)
                    success_msg = f"Updated '{item.name}' stock to {new_stock}"
                    print(f"Success: {success_msg}")
                    self._log_action(success_msg)
                except ValueError as e:
                    print(f"Error: {e}")
                return
        print(f"Error: Product with SKU '{sku}' not found!")

    # ==========================================
    # Integration with Task 2 Features
    # ==========================================
    def search_by_prefix(self, prefix: str):
        """Utilize the Trie to perform blazing fast prefix matching."""
        print(f"\n🔍 Searching for prefix: '{prefix}'")
        results = self.sku_trie.search_by_prefix(prefix)
        if not results:
            print("No matching products found.")
        else:
            for item in results:
                print(" ->", item.display_info())

    def show_low_stock_alerts(self):
        """Utilize Heap Sort to display items ordered by lowest stock."""
        print("\n⚠️ Low Stock Alert (Sorted by Heap Sort) ⚠️")
        # Create a shallow copy to avoid modifying the main inventory order
        inventory_copy = self.inventory.copy()
        sorted_inventory = heap_sort_by_stock(inventory_copy)
        
        for item in sorted_inventory:
            print(f"Stock: {item.get_stock()} | {item.name} ({item.get_sku()})")