<?php
//interface for PassedDates Database connection
interface PassedDateInt{
	public function getAllEntries(): array; // returns alll entries 
	public function getFromLimited(DateTime $Begin,int $limits): array;//returns entries from begin and limits its to limits
	public function getNewestLimited(int $limits):array; //returns the newes Limits entries fromt the database
}