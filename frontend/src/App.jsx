import { useEffect, useState } from 'react';
import csvFile from './assets/updated_data.csv';
import { Select, Option, Button } from "@material-tailwind/react";
import {getTags} from './services/api';

function App() {
  const [csvData, setCsvData] = useState([]);
  const [csvHeaders, setCsvHeaders] = useState([]);

  // useEffect(() => {
  //   fetch(csvFile)
  //     .then(response => response.text())
  //     .then(text => {
  //       const rows = text.split('\n');
  //       const headers = rows[0].split(',');
  //       // remove last 2 columns
  //       headers.splice(headers.length - 2, 2);
  //       setCsvHeaders(headers);
  //       const data = rows.slice(1).map(row => {
  //         if (row === '') {
  //           return null;
  //         }
  //         const tempValues = row.split(',"');
  //         // console.log(tempValues);
  //         const Name = tempValues[0];
  //         const tempValues2 = tempValues[1].split('",');
  //         const Address = tempValues2[0];
  //         const tempValues3 = tempValues2[1].split(',');
  //         const eachRow = {};
  //         headers.forEach((header, index) => {
  //           if (index === 0) {
  //             eachRow[header] = Name;
  //           }
  //           else if (index === 1) {
  //             eachRow[header] = Address;
  //           }
  //           else {
  //             eachRow[header] = tempValues3[index - 2];
  //           }
  //         });
  //         return eachRow;
  //       });
  //       setCsvData(data);
  //       // console.log(data);
  //     });
  // }, []);

  const [tags, setTags] = useState([]);

  useEffect(() => {
    getTags().then((res) => {
      console.log(res);
      setTags(res.data);
    });
  }, []);


  const [price, setPrice] = useState('Low');
  const priceOptions = ['Low', 'Medium', 'High'];

  const setPriceFilter = (e) => {
    // console.log(e);
    setPrice(e);
    console.log(price);
  }

  const [rating, setRating] = useState('Low');
  const ratingOptions = ['Low', 'Medium', 'High'];

  const setRatingFilter = (e) => {
    // console.log(e);
    setRating(e);
    console.log(rating);
  }

  return (
    <div className="App">
      <div className="bg-white p-8 rounded-md w-full">
        <h1 className="text-2xl font-bold w-full text-center mb-10">Welcome to the recommender system</h1>
        <div className=" flex items-center justify-between pb-6">
          <div className="flex gap-4">
            <Select variant="outlined" label="Select Price" onChange={setPriceFilter}>
              {priceOptions.map((item, index) => (
                <Option key={index} value={item}>
                  {item}
                </Option>
              ))}
            </Select>
            <Select variant="outlined" label="Select Rating" onChange={setRatingFilter}>
              {ratingOptions.map((item, index) => (
                <Option key={index} value={item}>
                  {item}
                </Option>
              ))}
            </Select>
            <Select variant="outlined" label="Select Price" onChange={setPriceFilter}>
              {priceOptions.map((item, index) => (
                <Option key={index} value={item}>
                  {item}
                </Option>
              ))}
            </Select>
          </div>
          <div className="flex items-center justify-between">

            <div className="lg:ml-40 ml-10 space-x-8">
              <Button color="lightBlue" buttonType="filled" size="regular" rounded={false} block={false} iconOnly={false} ripple="light">
                Get Recommendations
              </Button>
            </div>
          </div>
        </div>
        <div>
          <div className="-mx-4 sm:-mx-8 px-4 sm:px-8 py-4 overflow-x-auto">
            <div className="inline-block min-w-full shadow rounded-lg overflow-hidden">
              <table className="min-w-full leading-normal">
                <thead className='sticky top-0'>
                  <tr>
                    {csvHeaders.map(header => (
                      <th
                        key={header}
                        className="px-5 sticky top-0 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                        {header}
                      </th>
                    ))
                    }

                  </tr>
                </thead>
                <tbody>
                  {csvData && csvData.map((data, index) => (
                    <TableRow key={index} data={data} />
                  ))
                  }
                </tbody>
              </table>

            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

function TableRow(props) {
  const data = props.data;
  if (data === null) {
    return null;
  }
  const known = data['Known For'];
  return (
    <tr>
      {data && Object.keys(data).map((key, index) => (
        <td key={index} className="px-5 py-5 border-b border-gray-200 bg-white text-sm">
          <p className="text-gray-900 whitespace-no-wrap">
            {data[key]}
          </p>
        </td>
      ))
      }

    </tr>
  )
}

// const DropdownFilter = (data, value, onChange) => {
//   data = data.data
//   value = data.value
//   onChange = data.onChange
//   console.log(data);
//   const [value, setValue] = useState(data.value);
//   return (
//     <Select variant="outlined" label="Select Version">
//       {data.map((item, index) => (
//         <Option key={index} value={item}>
//           {item}
//         </Option>
//       ))}
//     </Select>
//   );
// }