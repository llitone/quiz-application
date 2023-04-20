using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http.Json;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Tele2App.Services
{
    public class PointsService
    {
        public async Task<bool> UpdatePoints(UpdatedUser user)
        {
            string endpoint = $"http://d1ffic00lt.com/app/api/v1.0/users/update/";
            HttpClient client = new HttpClient();
            
            var result = await client.PostAsync(endpoint, JsonContent.Create(user));

            return result.IsSuccessStatusCode;
        }
    }

    public class UpdatedUser
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }
        [JsonPropertyName("points")]
        public int Points { get; set; }
    }
}
