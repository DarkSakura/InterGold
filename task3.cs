public DataTable GetCustomerInfo(string id, string start_date = null, string end_date = null)
{
    var dt = new DataTable();
    using (var conn = new SqlConnection("...")) // Connection string is hardcoded
    {
        conn.Open();
        if (start_date.HasValue && end_date.HasValue)
        {
            var sql = "SELECT * FROM Customer WHERE id = '" + id + "' AND create_at BETWEEN DATE " + start_date + " AND DATE " + end_date;
        }
        else
        {
            var sql = "SELECT * FROM Customer WHERE id = '" + id + "'";
        }
        
        using (var da = new SqlDataAdapter(sql, conn))
        {
            da.Fill(dt);
        }
    }
    return dt;
}