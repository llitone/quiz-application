using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Tele2App.Model
{
    public class QuestionsData
    {
        [JsonPropertyName("question")]
        public List<Question> Questions { get; set; }
    }
}
