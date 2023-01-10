select * from movie;
create table moviecopy as select * from movie; 
delete from moviecopy;
select * from moviecopy;


DO $$
 DECLARE
     name_film	  channelcopy.film_name%TYPE;
     time_run     channelcopy.run_time%TYPE;
     years_cp   channelcopy.years%TYPE;
     rating channelcopy.rate%TYPE;

 BEGIN
 	 name_film := 'film-';
	 time_run := '2 h 00 min';
     years_cp := 1900;
     rating := 3.0;
     FOR counter IN 1..10
         LOOP
            INSERT INTO moviecopy (film_name, run_time, years, rate)
             VALUES (name_film || counter + 1, time_run + counter,  counter + 1, counter + 1);
         END LOOP;
 END;
 $$