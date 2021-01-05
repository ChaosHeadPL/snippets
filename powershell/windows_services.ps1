# script for managing SentryBay (MyDesk) services

function status_SentryBay{
    Get-Service -Name MyDesk
    Get-Service -Name epinjectsvc
    Get-Service -Name *sbupdate*
}

function start_SentryBay{
    Start-Service MyDesk
    Start-Service epinjectsvc
    Start-Service sbupdate
}

function stop_SentryBay{
    Stop-Service MyDesk
    Stop-Service epinjectsvc
    Stop-Service sbupdate
}

status_SentryBay