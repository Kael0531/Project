class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.product = None  # Store reference to the product object

class SKUTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, product) -> None:
        """Insert a product's SKU into the Trie."""
        node = self.root
        for char in product.get_sku():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.product = product

    def search_by_prefix(self, prefix: str) -> list:
        """Return a list of products whose SKUs match the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return [] # Prefix not found
            node = node.children[char]
        return self._collect_all_products(node)

    def _collect_all_products(self, node: TrieNode) -> list:
        """Helper method to recursively collect products from a node."""
        results = []
        if node.is_end_of_word:
            results.append(node.product)
        for child in node.children.values():
            results.extend(self._collect_all_products(child))
        return results

# ==========================================
# Task 2 Algorithm: Heap Sort
# ==========================================
def heapify(arr: list, n: int, i: int) -> None:
    """Build a max heap based on stock levels to sort ascendingly."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left].get_stock() > arr[largest].get_stock():
        largest = left
    if right < n and arr[right].get_stock() > arr[largest].get_stock():
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort_by_stock(arr: list) -> list:
    """Sort the product list by stock level in ascending order."""
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # Swap
        heapify(arr, i, 0)
    return arr