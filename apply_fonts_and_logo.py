import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

STYLE_INJECTION = """
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    body, h1, h2, h3, h4, h5, p, span, div, a, button, input, .font-sans, .font-serif, .bebas, .barlow-c, .nav-logo, .sb-logo {
      font-family: 'Google Sans', 'Plus Jakarta Sans', sans-serif !important;
    }
    h1, h2, h3, h4, h5, .nav-logo, .sb-logo, .font-bold, strong, b {
      letter-spacing: -0.02em !important;
    }
  </style>
"""

LOGO_IMG = '<img src="images/logo.png" alt="Logo" class="h-8 md:h-10 w-auto">'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject fonts
    if 'Plus Jakarta Sans' not in content:
        content = re.sub(r'(</head>)', STYLE_INJECTION + r'\n\1', content, flags=re.IGNORECASE)

    # 2. Replace icon logos in navbars (mostly <i class="ti ti-brand-abstract..."></i> followed by CLUB.OF.1986 or just alone)
    # The desktop navbar icon:
    content = re.sub(r'<i class="ti ti-brand-abstract[^"]*text-3xl[^"]*"></i>', LOGO_IMG, content)
    # The mobile sidebar icon:
    content = re.sub(r'<i class="ti ti-brand-abstract[^"]*text-2xl text-blue-800[^"]*"></i>', LOGO_IMG, content)
    # Generic brand abstract if it's inside a flex items-center next to CLUB.OF.1986 (let's use a specific regex)
    content = re.sub(r'<a href="index.html" class="flex items-center[^"]*">\s*<i class="ti ti-brand-abstract[^"]*"></i>\s*<span', r'<a href="index.html" class="flex items-center text-[#0A6BAA]">\n        ' + LOGO_IMG + r'\n        <span', content)

    # In checkout.html and others
    content = re.sub(r'<a href="index.html"[^>]*>\s*<i class="ti ti-brand-abstract[^"]*"></i>\s*</a>', f'<a href="index.html" class="flex items-center">\n        {LOGO_IMG}\n      </a>', content)

    # 3. Replace text logos in akun-saya, cek-resi, tata-cara-belanja, homepage
    content = re.sub(r'<div class="nav-logo">CLUB<span>.</span>OF<span>.</span>1986</div>', f'<div class="nav-logo">{LOGO_IMG}</div>', content)
    content = re.sub(r'<div class="sb-logo">CLUB<span>.</span>OF<span>.</span>1986</div>', f'<div class="sb-logo">{LOGO_IMG}</div>', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied logo and fonts successfully.")
