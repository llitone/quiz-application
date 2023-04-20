using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Tele2App.Model
{
    public class Answer
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }
        [JsonPropertyName("question_id")]
        public int QuestionId { get; set; }
        [JsonPropertyName("answer")]
        public string Text { get; set; }
        [JsonPropertyName("is_correct")]
        public bool IsCorrect { get; set; }
    }
}
