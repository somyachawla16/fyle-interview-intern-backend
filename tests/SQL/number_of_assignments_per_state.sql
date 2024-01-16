-- Write query to get number of assignments for each state
select assignments.state, count(*) from assignments group by assignments.state;