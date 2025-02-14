<?php
// Retrieve values from the form
$input1 = escapeshellarg($_POST['input1']);
$input2 = escapeshellarg($_POST['input2']);
$operation = escapeshellarg($_POST['operation']);

// Call the Python script with the user inputs
$command = escapeshellcmd("python3 math_operations.py $input1 $input2 $operation");
$output = shell_exec($command);

// Display the output from the Python script
echo "<h2>Calculation Result:</h2>";
echo "<div>$output</div>";
?>
