from manager import InventoryManager

def main():
    manager = InventoryManager()
    
    while True:
        print("\n=== 📦 Cross-Border E-Commerce Inventory System ===")
        print("1. View All Inventory ")
        print("2. Update Product Stock ")
        print("3. Auto-Complete Search by SKU Prefix ")
        print("4. Low Stock Alert Report ")
        print("5. View System Action Logs")
        print("6. Exit System")
        print("==================================================")
        
        choice = input("Please select an operation (1-6): ")
        
        if choice == '1':
            manager.show_all_products()
            
        elif choice == '2':
            sku = input("Enter Product SKU (e.g., EL-001): ").upper()
            try:
                new_stock = int(input("Enter new stock quantity: "))
                manager.update_stock(sku, new_stock)
            except ValueError:
                print("Invalid input! Stock must be an integer.")
                
        elif choice == '3':
            prefix = input("Enter SKU prefix (e.g., 'EL' or 'OUT'): ").upper()
            manager.search_by_prefix(prefix)
            
        elif choice == '4':
            manager.show_low_stock_alerts()
            
        elif choice == '5':
            print("\n--- System Audit Logs ---")
            for log in manager.action_logs:
                print(f"[*] {log}")
            print("-------------------------")
            
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
            
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()