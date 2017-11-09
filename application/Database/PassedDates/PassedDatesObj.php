<?php
//this is a data class wich hold date information with links and 
class PassedDateObj{
	private $name;
	private $date;
	private $link;
	private $text;
	public function __construct($name,$date,$link,$text){
		if($date instanceof DateTime){
			$this->date = $date;
		}
		else {
			$this->date = new DateTime('now');
		}
		if(is_string($link)){
			$this->link = $link;
		}
		else {
			$this->link = "";
		}
		if(is_string($name)){
			$this->name = $name;
		}
		else{
			$this->name = "";
		}
		if(is_string($text)){
			$this->text = $text;
		}
		else{
			$this->text = "";
		}
		
	}
	public function getName(): string{
		if( is_string($this->name)){
			return $this->name;
		}
		else {
			return "";
		}
	}
	public function getDate(): DateTime{
		if($this->date instanceof DateTime){
			return $this->date;
		}
		else{
			return new DateTime();
		}
	}
	public function getLink():string{
		return $this->link;
	}
	public function getText(): string{
		return $this->text;
	}
}