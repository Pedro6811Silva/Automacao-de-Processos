@echo off
chcp 65001 >nul 2>&1
title AdminBot - Automacao Administrativa

:: Verifica se o PowerShell está disponível
where powershell >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] PowerShell nao encontrado neste sistema.
    pause
    exit /b 1
)

:: Executa o script com política de execução liberada para o processo
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0AdminBot.ps1"

if %errorlevel% neq 0 (
    echo.
    echo [ERRO] O script terminou com erro. Verifique o arquivo adminbot.log.
    pause
)
