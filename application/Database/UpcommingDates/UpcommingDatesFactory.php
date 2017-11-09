<?php
include_once $_SERVER['DOCUMENT_ROOT']."/application/Database/UpcommingDates/UpcommingDatesSqlite.php";
class UpcommingDatesFactory{
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
	public function getUpcommingDatesConnection(){
		return new UpcommingDatesSqlite(); // this class which stands here represents the database interface
	}
}