<html>
    <body>
        <h2>Math Operations</h2>
        <form action="process_math.php" method="post">
            <label>Enter 1st number:</label>
            <input type="number" name="input1" required>
            <br>
            <label>Enter 2nd number:</label>
            <input type="number" name="input2" required>
            <br>
            <label>Select operation:</label>
            <select name="operation">
                <option value="add">Addition (+)</option>
                <option value="sub">Subtraction (-)</option>
                <option value="mul">Multiplication (×)</option>
                <option value="div">Division (÷)</option>
            </select>
            <br><br>
            <input type="submit" value="Calculate">
        </form>
    </body>
</html>