using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Tele2App.Model
{
    public class Question
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }
        [JsonPropertyName("age")]
        public int Age { get; set; }
        [JsonPropertyName("question")]
        public string Text { get; set; }
        [JsonPropertyName("difficulty")]
        public int Difficulty { get; set; }
        [JsonPropertyName("value")]
        public int Points { get; set; }
        [JsonPropertyName("subject_id")]
        public int SubjectId { get; set; }
        [JsonPropertyName("explanation")]
        public string Explanation { get; set; }
    }
}
