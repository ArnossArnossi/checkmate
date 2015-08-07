<?php


//boolean flag
class Foo {
    public function bar($flag = true) {
    }
}

//static access
class Foo
{
    public function bar()
    {
        Bar::baz();
    }
}


?>