
sequenceDiagram
    participant A as Administrator
    participant B as Server
    participant C as Prometheus Exporter
    participant D as Prometheus Server
    participant E as OpenTelemetry Collector
    participant F as Grafana Alloy

    A->>B: Install Exporter on the server
    A->>C: Configure Exporter (e.g., port, metrics)
    A->>D: Edit prometheus.yml (add Exporter)
    D->>C: Pull: Scrape metrics from Exporter
    A->>E: Install OpenTelemetry Collector
    A->>E: Configure OpenTelemetry Collector (receive from Prometheus, convert to OpenTelemetry)
    E->>F: Push: Send metrics to Grafana Alloy in OpenTelemetry format
