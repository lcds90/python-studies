from adapter import G3000LoaderAdapter
from loader import ReportLoader
from report import ReportAnalyzer


g3000_loader = ReportLoader()
loader = G3000LoaderAdapter(g3000_loader)
# o analyzer do nosso sistema recebe o adaptador como qualquer outro loader
analyzer = ReportAnalyzer(loader)
result = analyzer.average()  # Agora funcionará
print(result)
