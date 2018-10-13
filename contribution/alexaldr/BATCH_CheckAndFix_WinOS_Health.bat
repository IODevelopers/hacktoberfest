echo "\n\nSFC\n\n"
Sfc /scannow
echo "\n\ndism1\n\n"
Dism /online /cleanup-image /CheckHealth
Dism /online /cleanup-image /restorehealth
echo "\n\ndism2\n\n"