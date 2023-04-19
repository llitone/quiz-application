using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http.Json;
using System.Text;
using System.Threading.Tasks;
using Tele2App.Model;

namespace Tele2App.Services
{
    public class SubjectsService
    {
        private string _endpoint = "http://d1ffic00lt.com/app/api/v1.0/questions/";
        public async Task<IEnumerable<Subject>> GetSubjects()
        {
            HttpClient client = new HttpClient();
            var response = await client.GetAsync(_endpoint);
            var result = await response.Content.ReadFromJsonAsync<IEnumerable<Subject>>();
            return result;
        }
    }
}
