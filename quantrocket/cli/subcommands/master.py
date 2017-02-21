# Copyright 2017 QuantRocket - All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def add_subparser(subparsers):
    _parser = subparsers.add_parser("master", description="QuantRocket securities master CLI", help="quantrocket master -h")
    _subparsers = _parser.add_subparsers(title="subcommands", dest="subcommand")
    _subparsers.required = True

    parser = _subparsers.add_parser("download", help="Download security details from IB into securities master database")
    parser.add_argument("-e", "--exchange", required=True, metavar="EXCHANGE", help="the exchange code")
    parser.add_argument("-t", "--sec-type", dest="sec_type", default="STK", required=True, choices=["STK", "FUT", "CASH"], help="the security type")
    parser.add_argument("-c", "--currency", metavar="CURRENCY", help="limit to this currency")
    parser.add_argument("-s", "--symbols", nargs="*", metavar="SYMBOL", help="limit to these symbols")
    parser.add_argument("-g", "--groups", nargs="*", metavar="GROUP", help="limit to these groups")
    parser.add_argument("-i", "--conids", nargs="*", metavar="CONID", help="limit to these conids")
    parser.set_defaults(func="quantrocket.master.download_securities")

    parser = _subparsers.add_parser("marketdata", help="Load a snapshot of market data (e.g. liquidity) into securities master database to assist with group creation")
    parser.add_argument("-e", "--exchange", metavar="EXCHANGE", help="the exchange code")
    parser.add_argument("-t", "--sec-type", dest="sec_type", choices=["STK", "FUT", "CASH"], help="limit to this security type")
    parser.add_argument("-c", "--currency", metavar="CURRENCY", help="limit to this currency")
    parser.add_argument("-g", "--groups", nargs="*", metavar="GROUP", help="limit to these groups")
    parser.add_argument("-s", "--symbols", nargs="*", metavar="SYMBOL", help="limit to these symbols")
    parser.add_argument("-i", "--conids", nargs="*", metavar="CONID", help="limit to these conids")
    parser.add_argument("--sectors", nargs="*", metavar="SECTOR", help="limit to these sectors")
    parser.add_argument("--industries", nargs="*", metavar="INDUSTRY", help="limit to these industries")
    parser.add_argument("--categories", nargs="*", metavar="CATEGORY", help="limit to these categories")
    parser.set_defaults(func="quantrocket.master.load_marketdata")

    parser = _subparsers.add_parser("describe", help="View statistics about securities")
    parser.add_argument("-e", "--exchange", metavar="EXCHANGE", help="the exchange code")
    parser.add_argument("-t", "--sec-type", dest="sec_type", choices=["STK", "FUT", "CASH"], help="limit to this security type")
    parser.add_argument("-c", "--currency", metavar="CURRENCY", help="limit to this currency")
    parser.add_argument("-g", "--groups", nargs="*", metavar="GROUP", help="limit to these groups")
    parser.add_argument("-s", "--symbols", nargs="*", metavar="SYMBOL", help="limit to these symbols")
    parser.add_argument("-i", "--conids", nargs="*", metavar="CONID", help="limit to these conids")
    parser.add_argument("--sectors", nargs="*", metavar="SECTOR", help="limit to these sectors")
    parser.add_argument("--industries", nargs="*", metavar="INDUSTRY", help="limit to these industries")
    parser.add_argument("--categories", nargs="*", metavar="CATEGORY", help="limit to these categories")
    parser.set_defaults(func="quantrocket.master.describe_securities")

    parser = _subparsers.add_parser("get", help="Query security details from the securities master database")
    parser.add_argument("-e", "--exchange", metavar="EXCHANGE", help="the exchange code")
    parser.add_argument("-t", "--sec-type", dest="sec_type", choices=["STK", "FUT", "CASH"], help="limit to this security type")
    parser.add_argument("-c", "--currency", metavar="CURRENCY", help="limit to this currency")
    parser.add_argument("-g", "--groups", nargs="*", metavar="GROUP", help="limit to these groups")
    parser.add_argument("-s", "--symbols", nargs="*", metavar="SYMBOL", help="limit to these symbols")
    parser.add_argument("-i", "--conids", nargs="*", metavar="CONID", help="limit to these conids")
    parser.add_argument("--exclude-groups", nargs="*", metavar="GROUP", help="exclude these groups")
    parser.add_argument("--exclude-symbols", nargs="*", metavar="SYMBOL", help="exclude these symbols")
    parser.add_argument("--exclude-conids", nargs="*", metavar="CONID", help="exclude these conids")
    parser.add_argument("--sectors", nargs="*", metavar="SECTOR", help="limit to these sectors")
    parser.add_argument("--industries", nargs="*", metavar="INDUSTRY", help="limit to these industries")
    parser.add_argument("--categories", nargs="*", metavar="CATEGORY", help="limit to these categories")
    parser.add_argument("--delisted", action="store_true", default=False, help="include delisted securities")
    parser.set_defaults(func="quantrocket.master.get_securities")

    parser = _subparsers.add_parser("diff", help="Flag security details that have changed since the time they were loaded")
    parser.add_argument("-e", "--exchange", metavar="EXCHANGE", help="limit to this exchange")
    parser.add_argument("-t", "--sec-type", dest="sec_type", choices=["STK", "FUT", "CASH"], help="limit to this security type")
    parser.add_argument("-c", "--currency", metavar="CURRENCY", help="limit to this currency")
    parser.add_argument("-g", "--groups", nargs="*", metavar="GROUP", help="limit to these groups")
    parser.add_argument("-s", "--symbols", nargs="*", metavar="SYMBOL", help="limit to these symbols")
    parser.add_argument("-i", "--conids", nargs="*", metavar="CONID", help="limit to these conids")
    parser.add_argument("--sectors", nargs="*", metavar="SECTOR", help="limit to these sectors")
    parser.add_argument("--industries", nargs="*", metavar="INDUSTRY", help="limit to these industries")
    parser.add_argument("--categories", nargs="*", metavar="CATEGORY", help="limit to these categories")
    parser.add_argument("-f", "--fields", nargs="*", metavar="FIELD", help="only diff against these fields")
    parser.add_argument("--delist-missing", action="store_true", default=False, help="auto-delist securities that are no longer available from IB")
    parser.add_argument("--delist-exchanges", metavar="EXCHANGE", nargs="*", help="auto-delist securities that associated with these exchanges")
    parser.set_defaults(func="quantrocket.master.diff_securities")

    parser = _subparsers.add_parser("export", help="Export security details from the securities master database")
    parser.add_argument("filename", metavar="OUTFILE", help="the filename to save the export to")
    parser.add_argument("-e", "--exchange", metavar="EXCHANGE", help="the exchange code")
    parser.add_argument("-t", "--sec-type", dest="sec_type", choices=["STK", "FUT", "CASH"], help="limit to this security type")
    parser.add_argument("-c", "--currency", metavar="CURRENCY", help="limit to this currency")
    parser.add_argument("-g", "--groups", nargs="*", metavar="GROUP", help="limit to these groups")
    parser.add_argument("-s", "--symbols", nargs="*", metavar="SYMBOL", help="limit to these symbols")
    parser.add_argument("-i", "--conids", nargs="*", metavar="CONID", help="limit to these conids")
    parser.add_argument("-n", "--min-liq", metavar="DOLLAR_VOLUME", type=int, help="limit to symbols where 90-day price X volume is greater than or equal to this number")
    parser.add_argument("-x", "--max-liq", metavar="DOLLAR_VOLUME", type=int, help="limit to symbols where 90-day price X volume is less than or equal to this number")
    parser.add_argument("--exclude-groups", nargs="*", metavar="GROUP", help="exclude these groups")
    parser.add_argument("--exclude-symbols", nargs="*", metavar="SYMBOL", help="exclude these symbols")
    parser.add_argument("--sectors", nargs="*", metavar="SECTOR", help="limit to these sectors")
    parser.add_argument("--industries", nargs="*", metavar="INDUSTRY", help="limit to these industries")
    parser.add_argument("--categories", nargs="*", metavar="CATEGORY", help="limit to these categories")
    parser.add_argument("--tws", dest="tws", action="store_true", help="Format output for TWS import")
    parser.set_defaults(func="quantrocket.master.export_securities")

    parser = _subparsers.add_parser("group", help="Create a group of securities meeting certain criteria")
    parser.add_argument("name", metavar="GROUP_NAME", help="the name to assign to the group")
    parser.add_argument("-e", "--exchange", metavar="EXCHANGE", help="limit to this exchange")
    parser.add_argument("-t", "--sec-type", dest="sec_type", choices=["STK", "FUT", "CASH"], help="limit to this security type")
    parser.add_argument("-c", "--currency", metavar="CURRENCY", help="limit to this currency")
    parser.add_argument("-n", "--min-liq", metavar="DOLLAR_VOLUME", type=int, help="limit to symbols where 90-day price X volume is greater than or equal to this number")
    parser.add_argument("-x", "--max-liq", metavar="DOLLAR_VOLUME", type=int, help="limit to symbols where 90-day price X volume is less than or equal to this number")
    parser.add_argument("--from-groups", nargs="*", metavar="GROUP", help="limit to symbols from these existing groups")
    parser.add_argument("-s", "--symbols", nargs="*", metavar="SYMBOL", help="limit to these symbols")
    parser.add_argument("-i", "--conids", nargs="*", metavar="CONID", help="limit to these conids")
    parser.add_argument("--sectors", nargs="*", metavar="SECTOR", help="limit to these sectors")
    parser.add_argument("--industries", nargs="*", metavar="INDUSTRY", help="limit to these industries")
    parser.add_argument("--categories", nargs="*", metavar="CATEGORY", help="limit to these categories")
    parser.add_argument("-f", "--input-file", metavar="FILENAME", help="create the group from the con_ids in this file")
    parser.add_argument("-a", "--append", action="store_true", help="append to group if group already exists")
    parser.set_defaults(func="quantrocket.master.create_group")

    parser = _subparsers.add_parser("rmgroup", help="Remove a security group")
    parser.add_argument("group", help="the group name")
    parser.set_defaults(func="quantrocket.master.delete_group")

    parser = _subparsers.add_parser("delist", help="Delist a security by con_id or symbol+exchange")
    parser.add_argument("-c", "--conid", type=int, help="the conid of the security to delist")
    parser.add_argument("-s", "--symbol", help="the symbol to be delisted")
    parser.add_argument("-e", "--exchange", help="the exchange of the symbol to be delisted")
    parser.set_defaults(func="quantrocket.master.delist")
