
After we forked Arelle we made the following changes

# Changed files
* arelle\plugin\xbrlDB\sql\semantic\xbrlSemanticOracleDB.sql
	* I change bigint to NUMBER(19) according to https://docs.oracle.com/cd/B19306_01/gateways.102/b14270/apa.htm
	* remove  / erroneous located after CREATE INDEX root_index02 causing previous statement to rerun
	* change entity_identifier table definition primary key from entity_id to entity_identifier_id
	* change insert trigger for entity_identifier
	* CREATE SEQUENCE seq_entity used by entity table trigger
	* I removed all the double quotes surrounding the name of the objects (tables, triggers, etc) because in oracle that forces all the name to be in lower case and that is a problem because if you don’t put a name in double quotes then by default oracle translates it to upper case. For example
		* Create table “aaa” ..;
		* Select * from aaa -> table or view does not exist
		* Select * from AAA -> table or view does not exist
		* Select * from “aaa” -> results OK
	* And even in the plugin code there were failures because of this because some times tables where refered without double quotes. An other approach would be to correct the code by adding double quotes at every reference, but I don’t suggest that because in oracle creating tables in double quotes is a bad practice.
	* There was a side effect of that change resource cannot be used as a table name because it is reserved so I renamed it to xresource
	* I removed drop commands because they are dangerous for deleting all data by mistake
* arelle\plugin\xbrlDB\SqlDb.py
	* line 268 dbTableName I comment out double quotes addition
	* 320 the command in oracle is lock table not lock
	* 498 select trigger_name FROM user_triggers (not show)
	* 508 and an upper
* arelle\plugin\xbrlDB\XbrlSemanticSqlDB.py
	* line 95,783   I changed resource to xresource  (see comments on xbrlSemanticOracleDB.sql)
	* line 99  	   I removed the drop of the objects (the whole schema) in case of missing tables very dangerous. As Arelle suggests we must create the schema with xbrlSemanticOracleDB.sql script from sqlplus and not from the plugin. So I think it is wrong to recreate it from the plugin.
	*line 975,1046 startDatetime is filled with instant period startdate time because if it is null query fails 
* arelle\ModelInstanceObject.py
	* line 933   startDatetime is filled with istant and ti is not null see comment about startDatetime on XbrlSemanticsSqlDB.py 
	* line 951  	I removed addOneDay at end date because we dont want the ednd date to be 1/1 of the next year instead of 31/12 
* arelle\CntlrCmdLine.py
	* line 153 προσθηκη παραμέτρου SeqNo
	* line 538 προσθηκη της seqNo στο log 
* arelle\CntlrWebMain.py
	* line 231   add SeqNo
	* line 235  	differentiate error messagew for empty file and no zip file  
* arelle\Version.py 	
	*line 26  get githash bypassed 

