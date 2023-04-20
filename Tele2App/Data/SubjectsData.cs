using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Tele2App.Model;

namespace Tele2App.Data
{
    public static class SubjectsData
    {
        private static List<Subject> _subjects;

        public static void SetSubjects(List<Subject> subjects)
        {
            _subjects = subjects;
        }

        public static List<Subject> GetSubjects()
        {
            return _subjects;
        }
    }
}
