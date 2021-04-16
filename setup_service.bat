rem setup_service.bat
call nssm.exe install syslog_server_python "%cd%\run_server.bat"
call nssm.exe set syslog_server_python AppStdout "%cd%\app_logs\syslog_server_python.log"
call nssm.exe set syslog_server_python AppStderr "%cd%\app_logs\syslog_server_python.log"
call sc start syslog_server_python