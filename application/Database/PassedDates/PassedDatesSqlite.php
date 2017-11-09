<?php
include_once $_SERVER['DOCUMENT_ROOT'].'/html/util/lib.php';
include_once $_SERVER['DOCUMENT_ROOT']."/application/Database/PassedDates/PassedDatesInt.php";
include_once $_SERVER['DOCUMENT_ROOT']."/application/Database/PassedDates/PassedDatesObj.php";

class PassedDatesSqlite implements PassedDateInt{
	private $Database = null;
	public function getAllEntries(): array{
		$stm = $this->Database->prepare("SELECT * from dates order by d_day desc");
		if(is_bool($stm)){
			//return empty arrow if statement creation failes
			print "DATABASE FAILED";
			return array();
		}
		$result = $stm->execute();
		if(!($result instanceof SQLite3Result)){
			return array();
		}
		else {
			$retval = array();
		}
		while( is_array($row = $result->fetchArray(SQLITE3_ASSOC))){
			$timestring = $this->Database->query("Select datetime(".$row['d_day'].")"); //make the time cast into a string
			$time = $timestring->fetchArray()[0];
			$timestring->finalize();
			$retval[] = new PassedDateObj($row['d_name'],new DateTime($time), $row['d_link_to_page'],$row['d_text'] );
		}
		return $retval; //returns the all Limits entries fromt the database
	}
	public function getFromLimited(DateTime $Begin,int $limits): array{
		$stm = $this->Database->prepare("SELECT * from dates where d_day BETWEEN julianday(':Date1') and julianday( ':Date2') order by d_day desc LIMIT :Limit");
		if(is_bool($stm)){
			//return empty arrow if statement creation failes
			print "DATABASE FAILED";
			return array();
		}
		$stm->bindValue(":Date1", $Begin->format("Y-m-d"));
		$now = new DateTime("now");
		$stm->bindValue(":Date2", $now->format("Y-m-d"));
		$result = $stm->execute();
		if(!($result instanceof SQLite3Result)){
			return array();
		}
		else {
			$retval = array();
		}
		while( is_array($row = $result->fetchArray(SQLITE3_ASSOC))){
			$timestring = $this->Database->query("Select datetime(".$row['d_day'].")"); //make the time cast into a string
			$time = $timestring->fetchArray()[0];
			$timestring->finalize();
			$retval[] = new PassedDateObj($row['d_name'],new DateTime($time), $row['d_link_to_page'],$row['d_text'] );
		}
		return  $retval;//returns entries from begin and limits its to limits
	}
	public function getNewestLimited(int $limits):array{
		//get the limit newest entries
		$stm = $this->Database->prepare("SELECT * from dates order by d_day desc LIMIT :Limit");
		if(is_bool($stm)){
			//return empty arrow if statement creation failes
			print "DATABASE FAILED";
			return array();
		}
		$stm->bindValue(':Limit', $limits,SQLITE3_INTEGER);
		$result = $stm->execute();
		if(!($result instanceof SQLite3Result)){
			return array();
		}
		else {
			$retval = array();
		}
		while( is_array($row = $result->fetchArray(SQLITE3_ASSOC))){
			$timestring = $this->Database->query("Select datetime(".$row['d_day'].")"); //make the time cast into a string
			$time = $timestring->fetchArray()[0];
			$timestring->finalize();
			$retval[] = new PassedDateObj($row['d_name'],new DateTime($time), $row['d_link_to_page'],$row['d_text'] );
		}
		return $retval; //returns the newes Limits entries fromt the database
	}
	public function __construct(){
		try{
			$this->Database = new SQLite3($_SERVER['DOCUMENT_ROOT']."/application/Database/database.sqlite3",SQLITE3_OPEN_READONLY);
		}catch (Exception $e){
			http_response_code(500);
			exit();
		}
	}
	
}