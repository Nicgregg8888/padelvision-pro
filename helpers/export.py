
from reportlab.pdfgen import canvas
import tempfile

def export_dashboard(stats):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(tmp.name)
    c.drawString(100, 800, "PadelVision Pro - Dashboard Report")
    y = 750
    for key, value in stats.items():
        c.drawString(100, y, f"{key}: {value}")
        y -= 20
    c.save()
    return tmp.name
