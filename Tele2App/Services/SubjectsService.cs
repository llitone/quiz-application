using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Tele2App.Model;

namespace Tele2App.Services
{
    public class SubjectsService
    {
        public async Task<IEnumerable<Question>> GetSubjectQuestions(string subjectName)
        {
            return new List<Question>();
        }

        public async Task<IEnumerable<string>> GetSubjects()
        {
            return new List<string>();
        }
    }
}
