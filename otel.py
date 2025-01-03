import json
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry import metrics

# Konfiguracja zasobów (Resource)
resource = Resource.create(attributes={
    "service.name": "sre-rest-service",
    "cmdbReference": "AT123",
    "opEnvironment": "DEV"
})

# Konfiguracja eksportera OTLP
exporter = OTLPMetricExporter(endpoint="https://alloy.lgtm.net/v1/metrics", insecure=False)

# Konfiguracja metryk
reader = PeriodicExportingMetricReader(exporter)
provider = MeterProvider(metric_readers=[reader], resource=resource)
metrics.set_meter_provider(provider)

# Pobierz Meter
meter = metrics.get_meter(__name__)

# Instrument do rejestrowania PID jako metryki
pid_gauge = meter.create_observable_gauge(
    name="process_pid",
    unit="1",
    description="Process ID"
)

# Przykładowy JSON
json_data = '''
{
  "pid": 123,
  "pmem": 10,
  "pcpu": 0.1,
  "name": "my_app",
  "command": "python3 my_app.py"
}
'''

# Przetwarzanie JSON
data = json.loads(json_data)

# Funkcja do zgłaszania metryki PID
def report_pid_callback(observer):
    observer.observe(
        value=data["pid"],
        attributes={
            "pmem": data["pmem"],
            "pcpu": data["pcpu"],
            "name": data["name"],
            "command": data["command"]
        }
    )

# Rejestracja funkcji zwrotnej
pid_gauge.add_callback(report_pid_callback)

print("Metryki zostały zgłoszone.")
