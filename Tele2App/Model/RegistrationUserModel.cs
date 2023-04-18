using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Tele2App.Model
{
    public class RegistrationUserModel
    {
        private string _password;

        [JsonPropertyName("name")]
        public string Name { get; set; }
        [JsonPropertyName("age")]
        public int Age { get; set; }
        [JsonPropertyName("phone_number")]
        public string PhoneNumber { get; set; }
        [JsonPropertyName("password")]
        public string Password
        {
            get { return _password; }
            set 
            {
                string buffer = value;
                SHA512 sha = SHA512.Create();
                var result = sha.ComputeHash(Encoding.UTF8.GetBytes(buffer));
                _password = Convert.ToBase64String(result);
            }
        }

        [JsonPropertyName("points")]
        public int Points { get; set; }
    }
}
