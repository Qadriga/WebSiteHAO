<?php
interface UpcommingDatesInt{
	public function getAllEntries():array;//return all entries
	public function getNewest($Limit):array; //get the limit newest entries
	public function getInMonth(DateInterval $Moth):array;
}