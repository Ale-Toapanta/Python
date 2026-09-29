$token = Read-Host "Pega tu token de SonarQube"

if ([string]::IsNullOrWhiteSpace($token)) {
    Write-Error "El token no puede estar vacío."
    exit 1
}

$env:SONAR_TOKEN = $token
$pysonar = "$env:LOCALAPPDATA\Python\pythoncore-3.14-64\Scripts\pysonar.exe"

if (-not (Test-Path $pysonar)) {
    Write-Error "No se encontró pysonar.exe en: $pysonar"
    exit 1
}

& $pysonar `
    --sonar-host-url=http://localhost:9000 `
    --sonar-token=$env:SONAR_TOKEN `
    --sonar-project-key=Prueba

if ($LASTEXITCODE -ne 0) {
    Write-Error "El análisis terminó con errores. Código: $LASTEXITCODE"
    exit $LASTEXITCODE
}
