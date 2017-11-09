<?php
include_once $_SERVER['DOCUMENT_ROOT'].'/application/Database/PassedDates/PassedDatesSqlite.php';
class PassedDatesFactory{
	/*
	 * the Factory is a Singelton Class 
	 */
	protected static $_instance = NULL;
	protected function __construct(){
		
	}
	protected function __clone(){
		/*
		 * do not allow to clone this class
		 */
	}
	public static function getInstance(){
		if(null == self::$_instance){
			self::$_instance = new self;
		}
		return self::$_instance;
	}
	public function getPassedDatesConnection(){
		return new PassedDatesSqlite(); // this class which stands here represents the database interface
	}
	
}