# SkippyAI

#Defining Local Environment for API
# Define the variable name and value
$variableName = "YOUR_VARIABLE_NAME"
$variableValue = "YOUR_VARIABLE_VALUE"
# Set the variable using New-Item
New-Item -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" -Name $variableName -Value $variableValue -Force
# Optionally, you can update the current session with the new variable
[Environment]::SetEnvironmentVariable($variableName, $variableValue, [System.EnvironmentVariableTarget]::Machine)