using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Tele2App.Model
{
    public class Subject
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }
        [JsonPropertyName("subject")]
        public string Name { get; set; }
        public IEnumerable<Question> Questions { get; set; }
    }
}
