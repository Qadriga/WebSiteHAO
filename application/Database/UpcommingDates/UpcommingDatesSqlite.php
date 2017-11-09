<?php
include_once $_SERVER['DOCUMENT_ROOT'].'/html/util/lib.php';
include_once $_SERVER['DOCUMENT_ROOT']."/application/Database/UpcommingDates/UpcommingDatesInt.php";
include_once $_SERVER['DOCUMENT_ROOT']."/application/Database/UpcommingDates/UpcommingDateObj.php";
/*
 * SQLite3 impelmentation of Database Connection for Upcomming Dates
 */
class UpcommingDatesSqlite implements UpcommingDatesInt{
	/** @var SQLite3*/
	private  $Database = NULL;
	public function getAllEntries():array{
	}//return all entries
	public function getNewest($Limit):array{
		//get the limit newest entries
		$stm = $this->Database->prepare("SELECT * from upcommingDates order by _date desc LIMIT :Limit");
		if(is_bool($stm)){
			//return empty arrow if statement creation failes
			print "DATABASE FAILED";
			return array();
		}
		$stm->bindValue(':Limit', $Limit,SQLITE3_INTEGER);
		$result = $stm->execute();
		if(!($result instanceof SQLite3Result)){
			return array();
		}
		else {
			$retval = array();
		}
		while( is_array($row = $result->fetchArray(SQLITE3_ASSOC))){
			$timestring = $this->Database->query("Select datetime(".$row['_date'].")"); //make the time cast into a string
			$time = $timestring->fetchArray()[0];
			$timestring->finalize();
			$retval[] = new UpcommingDate(new DateTime($time), $row['_link'], $row['_name']);
		}
		return $retval;
	}
	public function getInMonth(DateInterval $Moth):array{
		
	}
	public function __construct(){
		/*
		 * Constuctor for the Upcomming Dates Database Connecten using sqlite
		 */
		try {
			$this->Database = new SQLite3($_SERVER['DOCUMENT_ROOT'].'/application/Database/database.sqlite3',SQLITE3_OPEN_READONLY);
		} catch (Exception $e) {
			http_response_code(500);
			exit();
			//render('500','.html');// if the database is not found raise internal error 
		}
			
	}
	
}