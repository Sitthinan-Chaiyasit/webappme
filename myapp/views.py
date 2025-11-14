from django.shortcuts import render


def page(request):
	"""Simple page view that renders a friendly HTML page."""
	context = {
		'title': 'Nyxen',
		'message': 'ยินดีต้อนรับสู่หน้าเว็บตัวอย่างที่สร้างโดย ig : nnyxen.cy.',
		'icon_url': '/static/myapp/images/nyxen_icon.png',
	}
	return render(request, 'myapp/page.html', context)
