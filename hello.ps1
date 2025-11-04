# Get username and computer name
$user = $env:USERNAME
$pc = $env:COMPUTERNAME

# Display message
Write-Host "Hello $user! You are using $pc 😊"
