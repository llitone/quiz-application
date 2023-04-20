using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Tele2App.Data;
using Tele2App.Model;

namespace Tele2App.Services
{
    public class EverydayTasksService
    {
        public EverydayTasksService() { }

        public List<Question> GetTasks(int count)
        {
            List<Question> result = new List<Question>();
            var allSubjects = SubjectsData.GetSubjects();

            Random random = new Random();

            foreach(var subject in allSubjects)
            {
                if (count <= 0)
                    break;

                int index = random.Next(0, subject.Questions.Count());
                if (subject.Questions.Count() > 0)
                {
                    result.Add(subject.Questions.ElementAt(index));
                    count--;
                }
            }

            return result;
        }
    }
}
