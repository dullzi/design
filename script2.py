import re

with open('all-products.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change nav-sidebar to bottom sheet
nav_sidebar_old = """  <!-- Mobile Nav Sidebar -->
  <aside id="nav-sidebar"
    class="fixed inset-y-0 left-0 z-[100] w-[280px] bg-white transform -translate-x-full transition-transform duration-300 overflow-y-auto flex flex-col">"""
nav_sidebar_new = """  <!-- Mobile Nav Sidebar -->
  <aside id="nav-sidebar"
    class="fixed inset-x-0 bottom-0 top-auto z-[100] w-full max-h-[85vh] rounded-t-2xl bg-white transform translate-y-full transition-transform duration-300 overflow-y-auto flex flex-col">"""
content = content.replace(nav_sidebar_old, nav_sidebar_new)

# Update toggleMobileNav logic
nav_js_old = """        setTimeout(() => {
          overlay.classList.add('opacity-100');
          sidebar.classList.remove('-translate-x-full');
        }, 10);
      } else {
        sidebar.classList.add('-translate-x-full');"""
nav_js_new = """        setTimeout(() => {
          overlay.classList.add('opacity-100');
          sidebar.classList.remove('translate-y-full');
        }, 10);
      } else {
        sidebar.classList.add('translate-y-full');"""
content = content.replace(nav_js_old, nav_js_new)

# 2. Change filter-sidebar to bottom sheet
filter_sidebar_old = """      <aside id="filter-sidebar"
        class="fixed inset-y-0 left-0 z-[70] w-[280px] bg-white transform -translate-x-full transition-transform duration-300 overflow-y-auto lg:relative lg:translate-x-0 lg:z-auto lg:overflow-visible lg:flex-shrink-0 lg:block lg:bg-transparent shadow-2xl lg:shadow-none h-full lg:h-auto">"""
filter_sidebar_new = """      <aside id="filter-sidebar"
        class="fixed inset-x-0 bottom-0 top-auto z-[70] w-full max-h-[85vh] rounded-t-2xl bg-white transform translate-y-full transition-transform duration-300 overflow-y-auto lg:relative lg:translate-y-0 lg:z-auto lg:overflow-visible lg:flex-shrink-0 lg:w-[280px] lg:block lg:bg-transparent shadow-2xl lg:shadow-none h-full lg:h-auto lg:rounded-none">"""
content = content.replace(filter_sidebar_old, filter_sidebar_new)

# Update toggleMobileFilter logic
filter_js_old = """          function toggleMobileFilter() {
            const sidebar = document.getElementById("filter-sidebar");
            const overlay = document.getElementById("mobile-filter-overlay");
            sidebar.classList.toggle("-translate-x-full");
            overlay.classList.toggle("hidden");
            document.body.style.overflow = sidebar.classList.contains("-translate-x-full") ? "" : "hidden";
          }"""
filter_js_new = """          function toggleMobileFilter() {
            const sidebar = document.getElementById("filter-sidebar");
            const overlay = document.getElementById("mobile-filter-overlay");
            sidebar.classList.toggle("translate-y-full");
            overlay.classList.toggle("hidden");
            document.body.style.overflow = sidebar.classList.contains("translate-y-full") ? "" : "hidden";
          }"""
content = content.replace(filter_js_old, filter_js_new)


# 3. Replace cart-drawer with a floating cart widget that looks like the CS Chat
cart_drawer_pattern = r'<!-- Cart Drawer Overlay -->.*?function toggleCartSlide\(\) \{.*?\n\s*\}\n\s*</script>'
cart_floating_html = """  <div class="fixed bottom-6 right-6 md:bottom-8 md:right-8 z-[100] flex flex-col items-end">
    <!-- Cart Window Popup -->
    <div id="cart-drawer" class="hidden w-[340px] max-w-[calc(100vw-32px)] bg-white border border-[#E5E7EB] rounded-2xl shadow-2xl mb-4 flex-col h-[480px] max-h-[70vh] overflow-hidden transition-all duration-300 origin-bottom-right">
      <!-- Header -->
      <div class="bg-[#0A6BAA] text-white p-4 flex justify-between items-center">
        <h3 class="font-bold text-[15px] font-sans flex items-center gap-2">
          <i class="ti ti-shopping-cart text-xl"></i> Keranjang
        </h3>
        <button onclick="toggleCartSlide()" class="text-white/80 hover:text-white transition-colors">
          <i class="ti ti-x text-xl"></i>
        </button>
      </div>
      
      <!-- Body -->
      <div class="flex-grow overflow-y-auto p-4 flex flex-col gap-4">
        <!-- Cart Item 1 -->
        <div class="flex gap-3 items-center border-b border-gray-100 pb-4">
          <div class="w-16 h-16 bg-gray-50 rounded border border-gray-100 flex items-center justify-center p-1 flex-shrink-0">
            <img src="images/product/foto jacket 1 -allproduct.webp" alt="Jacket" class="w-full h-full object-contain mix-blend-multiply">
          </div>
          <div class="flex-grow min-w-0">
            <h4 class="text-xs font-bold text-gray-800 truncate font-sans">Vintage Denim Jacket</h4>
            <p class="text-[10px] text-gray-500 mb-1">Size: M</p>
            <div class="text-xs font-bold text-[#0A6BAA]">Rp. 450.000</div>
          </div>
          <div class="text-xs font-bold text-gray-500 bg-gray-100 px-2 py-1 rounded">x1</div>
        </div>
        <!-- Cart Item 2 -->
        <div class="flex gap-3 items-center border-b border-gray-100 pb-4">
          <div class="w-16 h-16 bg-gray-50 rounded border border-gray-100 flex items-center justify-center p-1 flex-shrink-0">
            <img src="images/product/kaos 2 -allproduct.webp" alt="T-Shirt" class="w-full h-full object-contain mix-blend-multiply">
          </div>
          <div class="flex-grow min-w-0">
            <h4 class="text-xs font-bold text-gray-800 truncate font-sans">Striped Polo Shirt</h4>
            <p class="text-[10px] text-gray-500 mb-1">Size: L</p>
            <div class="text-xs font-bold text-[#0A6BAA]">Rp. 200.000</div>
          </div>
          <div class="text-xs font-bold text-gray-500 bg-gray-100 px-2 py-1 rounded">x2</div>
        </div>
      </div>
      
      <!-- Footer Input -->
      <div class="p-4 border-t border-gray-100 bg-gray-50">
        <div class="flex justify-between items-center mb-4">
          <span class="text-gray-600 font-medium text-sm">Total:</span>
          <span class="font-bold text-[#0A6BAA] text-lg">Rp. 850.000</span>
        </div>
        <button onclick="window.location.href='cart.html'" class="w-full py-3 bg-[#0A6BAA] text-white font-bold rounded hover:bg-[#085d96] transition-colors flex justify-center items-center gap-2">
          Lanjut ke Pembayaran <i class="ti ti-arrow-right"></i>
        </button>
      </div>
    </div>
    
    <!-- Floating Cart Button -->
    <button onclick="toggleCartSlide()" class="w-14 h-14 md:w-16 md:h-16 bg-[#5ba4cf] hover:bg-[#0A6BAA] text-white rounded-[16px] md:rounded-[20px] shadow-lg flex items-center justify-center transition-transform hover:scale-105 active:scale-95 border-2 border-white/20">
      <i class="ti ti-shopping-cart text-3xl md:text-4xl relative">
        <span class="absolute -top-1 -right-2 bg-red-500 text-white text-[10px] font-bold w-5 h-5 flex items-center justify-center rounded-full border-2 border-white">2</span>
      </i>
    </button>
  </div>

  <script>
    function toggleCartSlide() {
      const win = document.getElementById('cart-drawer');
      if (win.classList.contains('hidden')) {
        win.classList.remove('hidden');
        win.classList.add('flex');
      } else {
        win.classList.add('hidden');
        win.classList.remove('flex');
      }
    }
  </script>"""

content = re.sub(cart_drawer_pattern, cart_floating_html, content, flags=re.DOTALL)

with open('all-products.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modifications applied successfully.")
