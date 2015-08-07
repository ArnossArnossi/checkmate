<?php

//unused private field
cass Something
{
    private static $FOO = 2; // Unused
    private $i = 5; // Unused
    private $j = 6;
    public function addOne()
    {
        return $this->j++;
    }
}


//unused local var
class Foo {
    public function doSomething()
    {
        $i = 5; // Unused
    }
}


//unused private method
class Something
{
    private function foo() {} // unused
}


//unused formal parameter
class Foo
{
    private function bar($howdy)
    {
        // $howdy is not used
    }
}

?>