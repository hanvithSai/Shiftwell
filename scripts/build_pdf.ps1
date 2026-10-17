# Renders report/report.html to report/Shiftwell_Submission.pdf with headless Edge.
$edge = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
$dir  = Join-Path (Split-Path $PSScriptRoot -Parent) 'report'
$pdf  = Join-Path $dir 'Shiftwell_Submission.pdf'
if (Test-Path $pdf) { Remove-Item $pdf }
$url = 'file:///' + ($dir -replace '\\', '/') + '/report.html'
Start-Process $edge -ArgumentList '--headless', '--disable-gpu', '--no-pdf-header-footer', "--print-to-pdf=$pdf", $url -Wait
Start-Sleep 2
Get-Item $pdf | Select-Object LastWriteTime, Length
