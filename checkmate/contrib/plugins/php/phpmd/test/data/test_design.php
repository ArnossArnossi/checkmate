<?php

//exit expression
class Foo {
    public function bar($param)  {
        if ($param === 42) {
            exit(23);
        }
    }
}


//eval expression
class Foo {
    public function bar($param)  {
        if ($param === 42) {
            eval('$param = 23;');
        }
    }
}


//goto statement
class Foo {
    public function bar($param)  {
        A:
        if ($param === 42) {
            goto X;
        }
        Y:
        if (time() % 42 === 23) {
            goto Z;
        }
        X:
        if (time() % 23 === 42) {
            goto Y;
        }
        Z:
        return 42;
    }
}


?>
