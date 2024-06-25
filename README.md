# Remix Programming Language
<p>The Remix Programming Language is a basic compiled programming language created using Python.</p>
<br />
<h2>Start: </h2>
<p>
  Run "main.py" and provide the path of which your program is in. For starters, you can run "program_example.txt" for quickstart.
</p>
<br/>
<h2>
  Full documentation:
</h2>
<h3>Key:</h3>
<ul>
  <li>[VARRIABLE_NAME_ACCESS] = $[VARRIABLE_NAME]</li>
  <li>[VARRIABLE_NAME] = Name of the varriable.</li>
  <li>[VARRIABLE_VALUE] = Value of the varriable. This includes strings and numbers.</li>
  <li>[MESSAGE] = Message of the statement.</li>
  <li>[VARRIABLE_SET_NAME] = Name of the varriable that will be set in an expression.</li>
  <li>[OPERATOR] = A mathmatical operator (*, +, -, /).</li>
  <li>[NUMBER] = A float or integer value.</li>
  <li>[CONDITIONAL_OPERATOR] = A conditional operator used in if statements. (!= or ==)</li>
  <li>[VALUE] = a value (etheir a string or a number).</li>
  <li>[LINE_COUNT] = the number of lines under a statement that the compilier counts (When compiled).</li>
  <li>[FUNCTION_NAME] = A function name.</li>
  <li>[REPEAT_COUNT] = The number of times a repeat statement would loop.</li>
</ul>
<h3>Output/Input functions: </h3>
<ul>
  <li>*log [MESSAGE] OR [VARRIABLE_NAME_ACCESS] - Displays a message on the console. Example: log $x or log Hello</li>
  <li>*input [VARRIABLE_NAME_ACCESS] - Sets response to the varriable mentioned. Example: input $x</li>
</ul>
<h3>Varriables:</h3>
<ul>
  <li>*var [VARRIABLE_NAME] = [VARRIABLE_VALUE] - Creates/assigns the [VARRIABLE_NAME] to the [VARRIABLE_VALUE]. Example: var x = 10 or var x = Hello</li>
  <li>*$[VARRIABLE_NAME] - Main way of accessing a varriable. Example: log $x or input $x</li>
  </ul>
<h3>String/Math functions:</h3>
  <ul>
  <li>*lower [VARRIABLE_NAME] - Lowercases the string value of the corresponding [VARRIABLE_VALUE] of the [VARRIABLE_NAME]. Otherwise, it returns an error. Example: lower x</li>
  <li>*upper [VARRIABLE_NAME] - Uppercases the string value of the corresponding [VARRIABLE_VALUE] of the [VARRIABLE_NAME]. Otherwise, it returns an error. Example: upper x</li>
  <li>*math [VARRIABLE_SET_NAME] [OPERATOR] [VARRIABLE_NAME] or [NUMBER]. Example: math $x * 10 (Result is that [X] will be multiplied by 10). math $x * $y (Result is that [X] will be multiplied by [Y]).</li>
    </ul>
<h3>String Syntax:</h3>
    <ul>
  <li>*Strings are declared like normal, with the exception that every space corresponds to a [_].</li>
   <li> - I_am_CPB</li>
  <li>*When strings are outputed or used, they will be shown as normal.</li>
   <li> - I am CPB</li>
      </ul>
<h3>Syntax Rules:</h3>
      <ul>
  <li>*ALWAYS add spaces when shown in the documentation.</li>
        </ul>
<h3>IF statements:</h3>
        <ul>
  <li>*if [VARRIABLE_NAME] or [VALUE] [CONDITIONAL_OPERATOR] [VARRIABLE_NAME] or [VALUE] [LINE_COUNT].</li>
  <li>*(==) - is equal to.</li>
  <li>*(!=) - not equal to.</li>
 <li> *Example 1:</li>
   <li>* if [X] == [Y] 1</li>
    <li> -log $x</li>
   <li>* if [X] does equal to [Y], then the compiler would run 1 line below the if statement.</li>
   <li>* The values could be also strings or numbers.</li>
  <li> * if [X] does not equal to [Y], then the compilier would ignore the entire statement.</li>
          </ul>
<h3>FUNCTION statements:</h3>
          <ul>
  <li>*function [FUNCTION_NAME] [LINE_COUNT].</li>
  <li> *The [FUNCTION_NAME] specified will be used to utilize this function.</li>
   <li>*The [LINE_COUNT] represents how long the function is.</li>
 <li> *call [FUNCTION_NAME] - runs the function based from it's [LINE_COUNT]</li>
 <li> *Example 1:</li>
   <li> *function say_hi 1</li>
   <li>  -log hi</li>
    <li> call say_hi</li>
  <li>   (Returns: hi)</li>
 <li>   *The compiler ran 1 line under the function.</li>
 <li>   *The function does not run until called.</li>
            </ul>
<h3>Statement syntax:</h3>
            <ul>
 <li> *(-) - used to signify to the compiler to not run the line on default, but only in the statement.</li>
              </ul>
<h3>Comments:</h3>
              <ul>
 <li> *(-) - when not used in a statement, it could also be utilized as a comment as well.</li>
                </ul>
<h3>Loop Statements:</h3>
                <ul>
  <li>*repeat [NUMBER] [LINE_COUNT] - repeats the code within [LINE_COUNT] lines below it.</li>
  </ul>
