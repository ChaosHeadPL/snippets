[SERVICE]
    Flush         5
    Daemon        Off
    Log_Level     info

[INPUT]
    Name          exec
    Command       ps -ef | grep my_app | grep -v grep | wc -l
    Interval_Sec  10
    Tag           my_app_process_count

[FILTER]
    Name          parser
    Match         my_app_process_count
    Key_Name      exec
    Parser        process_count_parser

[FILTER]
    Name          record_modifier
    Match         my_app_process_count
    Record        otel_metric_name process_count
    Record        otel_metric_type gauge
    Record        otel_metric_description "Number of processes for my_app"

[OUTPUT]
    Name          opentelemetry
    Match         my_app_process_count
    Host          127.0.0.1
    Port          4317
    Resource      service.name="my_app_monitoring"
