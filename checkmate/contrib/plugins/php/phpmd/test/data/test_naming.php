<?php

//short name
class Something {
    private $q = 15; // VIOLATION - Field
    public static function main( array $as ) {  // VIOLATION - Formal
        $r = 20 + $this->q; // VIOLATION - Local
    }
}


//long name
class Something {
    protected $reallyLongIntName = -3;  // VIOLATION - Field
    public static function main( array $argumentsList[] ) { // VIOLATION - Formal
        $otherReallyLongName = -5; // VIOLATION - Local
        for ($interestingIntIndex = 0;  // VIOLATION - For
             $interestingIntIndex < 10;
             $interestingIntIndex++ ) {
        }
    }
}


//short method
class ShortMethod {
    public function a( $index ) { // Violation
    }
}


//constructor/enclosing class
class MyClass {
     // this is bad because it is PHP 4 style
    public function MyClass() {}
    // this is good because it is a PHP 5 constructor
    public function __construct() {}
}


// boolean et method name
class Foo {
    /**
     * @return boolean
     */
    public function getFoo() {} // bad
    /**
     * @return bool
     */
    public function isFoo(); // ok
    /**
     * @return boolean
     */
    public function getFoo($bar); // ok, unless checkParameterizedMethods=true
}
?>